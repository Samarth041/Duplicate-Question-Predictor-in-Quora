from src.predict import predict_duplicate

def main():
    print("\n🔍 Duplicate Question Detector (CLI Test)\n")

    # Sample inputs
    q1 = input("Enter Question 1: ")
    q2 = input("Enter Question 2: ")

    # Prediction
    result = predict_duplicate(q1, q2)

    print("\n-----------------------------")
    print("RESULT:")
    print("-----------------------------")

    if result["is_duplicate"] == 1:
        print("❌ DUPLICATE QUESTIONS")
    else:
        print("✅ NOT DUPLICATE QUESTIONS")

    print(f"Probability: {result['probability']:.4f}")
    print("-----------------------------\n")


if __name__ == "__main__":
    main()