"""
Unit Tests for Healthcare Claims ETL
"""

import pytest
import pandas as pd
from src.etl import HealthcareETL

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'claim_id': [1, 2],
        'patient_name': ['Test Patient', 'Other Patient'],
        'amount': [1000.0, -50.0],
        'status': ['pending', 'pending']
    })

def test_extraction():
    etl = HealthcareETL()
    df = etl.extract_claims()
    assert not df.empty
    assert 'claim_id' in df.columns

def test_transformation(sample_data):
    etl = HealthcareETL(source_data=sample_data)
    df = etl.extract_claims()
    transformed_df = etl.transform_claims(df)
    
    # Assertions
    assert 'tax_amount' in transformed_df.columns
    assert 'total_amount' in transformed_df.columns
    assert all(transformed_df['status'] == 'PENDING')
    
    # Check that negative amounts were filtered out
    assert len(transformed_df) == 1
    assert transformed_df.iloc[0]['amount'] == 1000.0

def test_load():
    etl = HealthcareETL()
    df = etl.extract_claims()
    transformed_df = etl.transform_claims(df)
    result = etl.load_to_azure(transformed_df)
    assert result is True
