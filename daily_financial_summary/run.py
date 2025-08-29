from crewai import Flow

if __name__ == "_main_":
    flow = Flow.from_file("flow.yaml")
    result = flow.run()
    print("=== FLOW COMPLETED ===")
    print(result)