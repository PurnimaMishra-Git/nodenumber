import pandas as pd
import math

# Input data
data = {
    "VM Size": [
        "kc.2xlarge", "kc.4xlarge", "kc.9xlarge", "kc.12xlarge", "kc.18xlarge", "kc.24xlarge",
        "kc.large", "kc.xlarge", "km.2xlarge", "km.4xlarge", "km.8xlarge", "km.12xlarge",
        "km.large", "km.xlarge", "kr.2xlarge", "kr.4xlarge", "kr.large", "kr.xlarge"
    ],
    "CPU Request": [4, 8, 18, 24, 36, 48, 1, 2, 4, 8, 16, 24, 1, 2, 4, 8, 1, 2],
    "Memory Request": [8, 16, 36, 48, 72, 96, 2, 4, 16, 32, 64, 96, 2, 8, 32, 64, 8, 16],
}

# Target quota
target_cpu = 88  # in cores
target_memory = 60  # in GB

# Create DataFrame
df = pd.DataFrame(data)

# Function to calculate required nodes
def calculate_required_nodes(cpu_per_node, mem_per_node, target_cpu, target_memory):
    return math.ceil(max(target_cpu / cpu_per_node, target_memory / mem_per_node))

# Apply function
df["Required Nodes"] = df.apply(
    lambda row: calculate_required_nodes(row["CPU Request"], row["Memory Request"], target_cpu, target_memory),
    axis=1
)

# Filter for approx. 40 nodes
df_around_40 = df[(df["Required Nodes"] >= 38) & (df["Required Nodes"] <= 42)]

# Sort and show
df_around_40 = df_around_40[["VM Size", "CPU Request", "Memory Request", "Required Nodes"]].sort_values(by="Required Nodes")
print(df_around_40.to_string(index=False))
