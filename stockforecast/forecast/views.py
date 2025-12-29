from django.shortcuts import render
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import base64
from io import BytesIO

# Load SARIMA model
model_path = 'forecast/sarima_model.pkl'
with open(model_path, 'rb') as f:
    sarima_model = pickle.load(f)

def home(request):
    # 👉 Get months from user input
    if request.method == "POST":
        forecast_steps = int(request.POST.get("months", 12))
    else:
        forecast_steps = 12  # default

    # Forecast
    forecast = sarima_model.forecast(steps=forecast_steps)

    # Get last date
    try:
        last_date = sarima_model.data.endog.index[-1]
    except:
        last_date = pd.to_datetime("2025-12-01")

    forecast_dates = pd.date_range(
        start=last_date + pd.offsets.MonthBegin(),
        periods=forecast_steps,
        freq='MS'
    )

    # DataFrame
    df_forecast = pd.DataFrame({
        'Date': forecast_dates.strftime('%Y-%m'),
        'Avg_Monthly_Price': forecast
    })

    # Plot
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(df_forecast['Date'], df_forecast['Avg_Monthly_Price'], marker='o')
    ax.set_title(f"Next {forecast_steps} Months Forecast")
    ax.set_xlabel("Date")
    ax.set_ylabel("Avg Monthly Price")
    plt.xticks(rotation=45)

    buf = BytesIO()
    plt.tight_layout()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()
    plt.close()

    return render(request, 'forecast/home.html', {
        'forecast': df_forecast.to_dict('records'),
        'plot': image_base64,
        'months': forecast_steps
    })
