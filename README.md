# Segwise.ai QA Testing Assignment

This repository contains the deliverables for the Segwise.ai QA testing assignment, including manual testing findings, regression checklist, and automation scripts.

## Repository Contents

- `QA_Report.md` - Comprehensive QA testing report with identified bugs and UX issues
- `regression_checklist.md` - Detailed regression testing checklist for core dashboard components
- `test_dashboard.py` - Python automation script using Playwright for dashboard testing
- `requirements.txt` - Python dependencies for the automation script
- `README.md` - This file

## Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup
1. Clone this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   playwright install chromium
   ```

### Running the Automation Test
```bash
python test_dashboard.py
```

The script will:
1. Open the Segwise.ai login page
2. Log in with the provided test credentials
3. Navigate to the dashboard
4. Assert presence of key UI elements
5. Generate a test report and screenshot

## Test Results Summary

### Manual Testing Findings
- **5 issues identified** ranging from high to low priority
- **Primary blocker**: Forced onboarding flow prevents full dashboard testing
- **UX inconsistencies**: Account context mismatch, unclear button states
- **Positive observations**: Responsive chat support, clear progress indicators

### Automation Testing
- **Login flow**: Successfully automated
- **Dashboard navigation**: Functional with onboarding flow detection
- **Element assertions**: Comprehensive checks for key UI components
- **Screenshot capture**: Automated documentation of test state

## Key Limitations

Due to the application's onboarding requirements, comprehensive testing of the following features was not possible:
- Filters & Boards functionality
- Custom reports features
- Dashboard charts and metrics
- Data visualization components

## Recommendations

1. **Immediate**: Provide demo/test mode for QA evaluation
2. **Short-term**: Improve button state feedback and error handling
3. **Long-term**: Implement progressive onboarding with partial access options

## Assignment Completion Status

- ✅ Manual testing completed with 5 issues identified
- ✅ Regression checklist created for core components
- ✅ Python automation script implemented and tested
- ✅ GitHub repository created with all deliverables
- ✅ Documentation provided for setup and execution
