
import sys
sys.path.insert(0, "src")

from scheduler import (
    Wave,
    ALGOS,
    schedule,
    state_at,
    runners_released
)

waves = [
    Wave("21K Elite", 0, 8, 1, 40),
    Wave("10K", 2, 10, 2, 120),
    Wave("5K", 4, 6, 3, 200),
]

print("RUNNER STATE SIMULATION TEST")
print("=" * 40)

for algo in ALGOS:
    print(f"\nTesting algorithm: {algo}")

    result = schedule(waves, algo, quantum=5, switch=1)

    for k, wave in enumerate(waves):
        state = state_at(waves, result, k, result["end"])

        released = runners_released(
            waves, result, k, result["end"]
        )

        print(f"{wave.name}: {state}")
        print(f"Runners released: {released}/{wave.runners}")

    print("Test completed.")

print("\nALL TESTS COMPLETED!")

