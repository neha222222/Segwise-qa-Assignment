# Segwise.ai Dashboard - Regression Testing Checklist

## Pre-Testing Setup
- [ ] Verify test environment is accessible
- [ ] Confirm test credentials are valid (qa@segwise.ai / segwise_test)
- [ ] Clear browser cache and cookies
- [ ] Document browser version and environment details

## Authentication & Login Flow
- [ ] **Login Page Access**
  - [ ] Navigate to https://segwise.ai
  - [ ] Verify login page loads correctly
  - [ ] Check all form elements are visible and functional
  
- [ ] **Login Process**
  - [ ] Enter valid credentials
  - [ ] Verify login button functionality
  - [ ] Confirm successful authentication
  - [ ] Check redirect behavior after login
  
- [ ] **Login Error Handling**
  - [ ] Test invalid email format
  - [ ] Test incorrect password
  - [ ] Verify appropriate error messages
  - [ ] Check password visibility toggle (if available)

## Onboarding Flow
- [ ] **Onboarding Navigation**
  - [ ] Verify step progression indicators
  - [ ] Check step completion status
  - [ ] Test navigation between steps
  
- [ ] **Ad Network Selection**
  - [ ] Verify all ad network options are displayed
  - [ ] Check network categorization (Popular, Beta)
  - [ ] Test network selection functionality
  - [ ] Verify configuration modal behavior
  
- [ ] **Onboarding Completion**
  - [ ] Test "Next" button state management
  - [ ] Verify completion requirements are clear
  - [ ] Check final step completion

## Dashboard Core Components

### Navigation & Layout
- [ ] **Main Navigation**
  - [ ] Verify all navigation menu items are accessible
  - [ ] Test navigation between dashboard sections
  - [ ] Check active state indicators
  - [ ] Verify responsive behavior
  
- [ ] **User Account Context**
  - [ ] Verify correct user information display
  - [ ] Check account dropdown functionality
  - [ ] Test logout functionality

### Filters & Boards (When Accessible)
- [ ] **Filter Functionality**
  - [ ] Test date range filters
  - [ ] Verify metric filters
  - [ ] Check filter combination behavior
  - [ ] Test filter reset functionality
  
- [ ] **Board Management**
  - [ ] Verify board creation process
  - [ ] Test board editing capabilities
  - [ ] Check board deletion functionality
  - [ ] Test board sharing features
  
- [ ] **Data Visualization**
  - [ ] Verify chart rendering
  - [ ] Test chart interaction (zoom, hover, click)
  - [ ] Check data refresh functionality
  - [ ] Verify export capabilities

### Custom Reports (When Accessible)
- [ ] **Report Creation**
  - [ ] Test report builder interface
  - [ ] Verify metric selection options
  - [ ] Check dimension configuration
  - [ ] Test report preview functionality
  
- [ ] **Report Management**
  - [ ] Verify report saving process
  - [ ] Test report editing capabilities
  - [ ] Check report deletion functionality
  - [ ] Test report scheduling features
  
- [ ] **Report Export**
  - [ ] Test various export formats (PDF, CSV, etc.)
  - [ ] Verify export data accuracy
  - [ ] Check export download process

## User Interface & Experience
- [ ] **Responsive Design**
  - [ ] Test desktop layout (1920x1080)
  - [ ] Test tablet layout (768x1024)
  - [ ] Test mobile layout (375x667)
  - [ ] Verify touch interactions on mobile
  
- [ ] **Loading States**
  - [ ] Verify loading indicators appear appropriately
  - [ ] Check loading timeout handling
  - [ ] Test loading state cancellation
  
- [ ] **Error Handling**
  - [ ] Test network error scenarios
  - [ ] Verify error message clarity
  - [ ] Check error recovery options
  - [ ] Test offline behavior

## Performance Testing
- [ ] **Page Load Times**
  - [ ] Measure initial page load
  - [ ] Test dashboard data loading
  - [ ] Check chart rendering performance
  
- [ ] **Data Refresh**
  - [ ] Test automatic data refresh
  - [ ] Verify manual refresh functionality
  - [ ] Check refresh frequency settings

## Browser Compatibility
- [ ] **Chrome** (Latest)
  - [ ] Full functionality test
  - [ ] Performance verification
  
- [ ] **Firefox** (Latest)
  - [ ] Cross-browser compatibility
  - [ ] Feature parity check
  
- [ ] **Safari** (Latest)
  - [ ] macOS compatibility
  - [ ] Mobile Safari testing
  
- [ ] **Edge** (Latest)
  - [ ] Windows compatibility
  - [ ] Enterprise features

## Security Testing
- [ ] **Session Management**
  - [ ] Test session timeout
  - [ ] Verify logout functionality
  - [ ] Check session persistence
  
- [ ] **Data Protection**
  - [ ] Verify HTTPS usage
  - [ ] Check sensitive data handling
  - [ ] Test input validation

## Integration Testing
- [ ] **Ad Network Connections**
  - [ ] Test connection establishment
  - [ ] Verify data synchronization
  - [ ] Check connection status indicators
  
- [ ] **Data Accuracy**
  - [ ] Compare dashboard data with source
  - [ ] Verify calculation accuracy
  - [ ] Check data consistency across views

## Support Features
- [ ] **Help & Documentation**
  - [ ] Test help system accessibility
  - [ ] Verify documentation links
  - [ ] Check tutorial functionality
  
- [ ] **Chat Support**
  - [ ] Test chat widget functionality
  - [ ] Verify support availability
  - [ ] Check chat history persistence

## Regression Test Execution Notes

### Test Environment Requirements
- Stable internet connection
- Test data access or demo mode
- Multiple browser installations
- Screen recording capability for bug documentation

### Test Data Requirements
- Valid test account credentials
- Sample ad network data (or demo mode)
- Test report configurations
- Sample filter combinations

### Bug Reporting Template
For each identified issue:
- **Issue ID**: Unique identifier
- **Severity**: Critical/High/Medium/Low
- **Steps to Reproduce**: Detailed steps
- **Expected Result**: What should happen
- **Actual Result**: What actually happens
- **Environment**: Browser, OS, screen resolution
- **Screenshots/Videos**: Visual evidence
- **Workaround**: If available

### Test Completion Criteria
- [ ] All checklist items executed
- [ ] Critical and high-priority bugs documented
- [ ] Test results documented with evidence
- [ ] Regression test report generated
- [ ] Stakeholders notified of results

---

**Note**: This checklist should be updated as new features are added or existing features are modified. Regular review and maintenance of test cases ensures comprehensive coverage.
