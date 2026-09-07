from customer.pipeline import run_customer_pipeline
def test_run_customer_pipeline():
    result = run_customer_pipeline("data/customers.csv")
    assert "processed" in result
    assert "rejected" in result

def test_run_customer_pipeline_separates_rejected_customers():
    result = run_customer_pipeline("data/customers.csv")
    print(result)
    assert len(result['processed']) == 2
    assert len(result['rejected']) == 1