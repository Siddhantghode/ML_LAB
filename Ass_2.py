import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error

#DATASET
x=np.array([[1],[2],[3],[4],[5]])
y=np.array([3,4,2,5,6])

#TRAIN LINEAR REGRESSION MODEL
model=LinearRegression()
model.fit(x,y)

#PREDICTION
y_pred=model.predict(x)

#SCATTER PLOT AND REGRESSIO LINE
plt.figure(figsize=(8,5))
plt.scatter(x,y,color="blue",label="Actual Data")
plt.plot(x,y_pred,color="red",label="Regression Line")


# Residual Lines
for xi, yi, ypi in zip(x.flatten(), y, y_pred):
    plt.vlines(
        x=xi,
        ymin=yi,
        ymax=ypi,
        color='gray',
        linestyle='dashed'
    )

# Labels and Title
plt.xlabel("X (Independent Variable)")
plt.ylabel("Y (Dependent Variable)")
plt.title("Scatter Plot with Regression Line and Residuals")
plt.legend()
plt.grid(True)

# Display Plot
plt.show()

# Model Parameters
print("Intercept (β0):", model.intercept_)
print("Slope (β1):", model.coef_[0])

# Error Metrics
print("Mean Squared Error (MSE):", mean_squared_error(y, y_pred))
print("Mean Absolute Error (MAE):", mean_absolute_error(y, y_pred))
