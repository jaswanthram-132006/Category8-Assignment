def machine_failure_probability(prior, evidence_given_failure,
                                evidence_given_normal):
    evidence = (
        prior * evidence_given_failure
        + (1 - prior) * evidence_given_normal
    )

    if evidence == 0:
        return 0.0

    return (
        prior * evidence_given_failure
    ) / evidence


prior_failure = 0.10
high_vibration_given_failure = 0.80
high_vibration_given_normal = 0.15

probability = machine_failure_probability(
    prior_failure,
    high_vibration_given_failure,
    high_vibration_given_normal
)

print("Smart Manufacturing - Machine Failure Prediction")
print(f"Probability of failure: {probability * 100:.2f}%")