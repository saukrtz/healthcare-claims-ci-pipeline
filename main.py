#!/usr/bin/env python3
"""
Main Executable for Healthcare Claims ETL
Author: Antigravity (Senior Data Engineer)
"""

import sys
import logging
from src.etl import run_pipeline

# Setup production-grade logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)-8s | %(name)s | %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('pipeline.log')
    ]
)

logger = logging.getLogger("HealthcareMain")

def main():
    logger.info("Starting Healthcare Claims ETL Suite...")
    try:
        success = run_pipeline()
        if success:
            logger.info("Pipeline execution completed successfully.")
            sys.exit(0)
        else:
            logger.error("Pipeline failed during execution.")
            sys.exit(1)
    except Exception as e:
        logger.critical(f"Unhandled exception in main execution: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
