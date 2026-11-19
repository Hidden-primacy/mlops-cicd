from src.model import train_model
from sklearn.datasets import load_iris

if __name__ == '__main__':
    model, accuracy = train_model()
    prediction = int(model.predict([[5.1, 3.5, 1.4, 0.2]])[0])
    print(f'Test accuracy: {accuracy:.4f}')
    print(f'Predicted species: {load_iris().target_names[prediction]}')
