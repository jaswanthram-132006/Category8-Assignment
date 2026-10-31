def bayesian_diagnosis(prior, sensitivity, false_positive):
    evidence = (
        sensitivity * prior
        + false_positive * (1 - prior)
    )

    if evidence == 0:
        return 0.0

    posterior = (sensitivity * prior) / evidence
    return posterior


prior = 0.10
sensitivity = 0.90
false_positive = 0.05

probability = bayesian_diagnosis(
    prior, sensitivity, false_positive
)

print("Medical Diagnosis using Bayesian Reasoning")
print(f"Prior probability: {prior * 100:.2f}%")
print(f"Probability after positive test: {probability * 100:.2f}%")

if probability >= 0.50:
    print("Result: High probability of disease")
else:
    print("Result: Low probability of disease")