🔍 Project Overview

I developed a Stock Forecasting Web App that predicts average monthly prices for the next 12 months using a SARIMA time-series model, deployed with Django, and fully containerized using Docker.

🛠️ Tech Stack Used

Python

SARIMA (Statsmodels)

Django

Pandas, Matplotlib

Docker

Docker Hub

⚙️ Key Features

✅ SARIMA model trained on historical data
✅ Model saved & loaded using .pkl
✅ Django backend for predictions
✅ Forecast visualization using Matplotlib
✅ Clean UI with HTML & CSS
✅ Fully containerized app
✅ Docker image pushed to Docker Hub

View
<img width="1141" height="744" alt="Screenshot 2025-12-29 122514" src="https://github.com/user-attachments/assets/41acf56c-7805-49e3-abc8-5d6071a9fed3" />
<img width="1158" height="744" alt="Screenshot 2025-12-29 122556" src="https://github.com/user-attachments/assets/0ed77622-70b3-4366-94c9-d950dfe0cd54" />


📦 Deployment

The application is packaged into a Docker image and uploaded to Docker Hub, making it easy to run anywhere using a single command.

💡 What I Learned

Integrating ML models into Django

Handling time-series forecasting in production

Dockerizing ML web applications

Debugging real-world deployment issues

Writing clean, scalable project structure

This project helped me understand how machine learning models move from notebooks to real applications.

I’m continuously learning and improving — feedback and suggestions are welcome! 😊

how to run ?
1.run model file first.
2.then one pkl file is created.
3.past it inside stockforecast.

docker 
pull usig command
docker pull chethankiruvaase/stockforecast:latest
