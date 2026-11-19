from src.model import train_model


def test_model_accuracy():
    _, accuracy = train_model()
    assert accuracy >= 0.80, f"Accuracy {accuracy:.4f} is below threshold"


def test_prediction():
    model, _ = train_model()
    assert int(model.predict([[5.1, 3.5, 1.4, 0.2]])[0]) == 0


def test_intentional_failure():
    assert False
