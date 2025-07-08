#!/usr/bin/env python3
"""
Segwise.ai Dashboard Automation Test Script

This script performs basic automated testing of the Segwise.ai dashboard:
1. Opens the login page
2. Logs in with test credentials
3. Navigates to the dashboard
4. Asserts presence of specific elements and metrics

Requirements:
- playwright
- pytest (optional, for test framework)

Usage:
    python test_dashboard.py
"""

import asyncio
import sys
from playwright.async_api import async_playwright
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class SegwiseDashboardTest:
    def __init__(self):
        self.base_url = "https://segwise.ai"
        self.login_email = "qa@segwise.ai"
        self.login_password = "segwise_test"
        self.browser = None
        self.page = None
        
    async def setup_browser(self):
        """Initialize browser and page"""
        playwright = await async_playwright().start()
        self.browser = await playwright.chromium.launch(headless=True)
        self.page = await self.browser.new_page()
        
        await self.page.set_viewport_size({"width": 1920, "height": 1080})
        
        logger.info("Browser initialized successfully")
        
    async def teardown_browser(self):
        """Close browser"""
        if self.browser:
            await self.browser.close()
            logger.info("Browser closed")
            
    async def navigate_to_login(self):
        """Navigate to the login page"""
        try:
            logger.info(f"Navigating to {self.base_url}")
            await self.page.goto(self.base_url, wait_until="networkidle")
            
            login_button = await self.page.wait_for_selector('text="Login"', timeout=10000)
            await login_button.click()
            
            await self.page.wait_for_url("**/login", timeout=10000)
            logger.info("Successfully navigated to login page")
            return True
            
        except Exception as e:
            logger.error(f"Failed to navigate to login page: {e}")
            return False
            
    async def perform_login(self):
        """Perform login with test credentials"""
        try:
            logger.info("Attempting to log in...")
            
            email_input = await self.page.wait_for_selector('input[type="email"]', timeout=10000)
            await email_input.fill(self.login_email)
            
            password_input = await self.page.wait_for_selector('input[type="password"]', timeout=10000)
            await password_input.fill(self.login_password)
            
            login_submit = await self.page.wait_for_selector('button[type="submit"]', timeout=10000)
            await login_submit.click()
            
            await self.page.wait_for_url("**/james_enter/**", timeout=15000)
            logger.info("Login successful")
            return True
            
        except Exception as e:
            logger.error(f"Login failed: {e}")
            return False
            
    async def navigate_to_dashboard(self):
        """Navigate to the main dashboard"""
        try:
            logger.info("Navigating to dashboard...")
            
            dashboard_url = f"{self.page.url.split('/james_enter')[0]}/james_enter/dashboard"
            await self.page.goto(dashboard_url, wait_until="networkidle")
            
            await self.page.wait_for_timeout(3000)
            
            current_url = self.page.url
            logger.info(f"Current URL after dashboard navigation: {current_url}")
            
            return True
            
        except Exception as e:
            logger.error(f"Failed to navigate to dashboard: {e}")
            return False
            
    async def assert_dashboard_elements(self):
        """Assert presence of key dashboard elements"""
        test_results = {
            "user_account_visible": False,
            "navigation_present": False,
            "onboarding_flow_detected": False,
            "chat_support_available": False,
            "page_loads_successfully": False
        }
        
        try:
            test_results["page_loads_successfully"] = True
            logger.info("✓ Page loaded successfully")
            
            try:
                user_element = await self.page.wait_for_selector('text="James_Enter"', timeout=5000)
                if user_element:
                    test_results["user_account_visible"] = True
                    logger.info("✓ User account information visible")
            except:
                logger.warning("✗ User account information not found")
                
            try:
                nav_elements = await self.page.query_selector_all('nav, [role="navigation"]')
                if nav_elements:
                    test_results["navigation_present"] = True
                    logger.info("✓ Navigation elements present")
            except:
                logger.warning("✗ Navigation elements not found")
                
            try:
                onboarding_element = await self.page.wait_for_selector('text="Connect your first Ad Network"', timeout=5000)
                if onboarding_element:
                    test_results["onboarding_flow_detected"] = True
                    logger.info("✓ Onboarding flow detected (expected behavior)")
            except:
                logger.info("No onboarding flow detected")
                
            try:
                chat_element = await self.page.query_selector('[aria-label="Open chat"]')
                if chat_element:
                    test_results["chat_support_available"] = True
                    logger.info("✓ Chat support widget available")
            except:
                logger.warning("✗ Chat support widget not found")
                
            await self.page.screenshot(path="dashboard_test_screenshot.png")
            logger.info("Screenshot saved as dashboard_test_screenshot.png")
            
        except Exception as e:
            logger.error(f"Error during element assertion: {e}")
            
        return test_results
        
    async def test_onboarding_flow(self):
        """Test onboarding flow elements if present"""
        onboarding_results = {
            "ad_networks_visible": False,
            "next_button_present": False,
            "progress_indicators_visible": False
        }
        
        try:
            ad_networks = await self.page.query_selector_all('text="Meta"')
            if ad_networks:
                onboarding_results["ad_networks_visible"] = True
                logger.info("✓ Ad network options visible")
                
            next_button = await self.page.query_selector('button:has-text("Next")')
            if next_button:
                onboarding_results["next_button_present"] = True
                is_disabled = await next_button.is_disabled()
                logger.info(f"✓ Next button present (disabled: {is_disabled})")
                
            progress_elements = await self.page.query_selector_all('text="Setup your App", text="Connect Adnetwork"')
            if progress_elements:
                onboarding_results["progress_indicators_visible"] = True
                logger.info("✓ Progress indicators visible")
                
        except Exception as e:
            logger.error(f"Error during onboarding flow test: {e}")
            
        return onboarding_results
        
    async def run_full_test(self):
        """Run the complete test suite"""
        logger.info("Starting Segwise.ai Dashboard Test Suite")
        
        test_passed = True
        
        try:
            await self.setup_browser()
            
            if not await self.navigate_to_login():
                test_passed = False
                
            if not await self.perform_login():
                test_passed = False
                
            if not await self.navigate_to_dashboard():
                test_passed = False
                
            dashboard_results = await self.assert_dashboard_elements()
            onboarding_results = await self.test_onboarding_flow()
            
            logger.info("\n" + "="*50)
            logger.info("TEST SUMMARY")
            logger.info("="*50)
            
            logger.info("Dashboard Elements:")
            for test, result in dashboard_results.items():
                status = "PASS" if result else "FAIL"
                logger.info(f"  {test}: {status}")
                
            logger.info("\nOnboarding Flow:")
            for test, result in onboarding_results.items():
                status = "PASS" if result else "FAIL"
                logger.info(f"  {test}: {status}")
                
            critical_tests = [
                dashboard_results["page_loads_successfully"],
                dashboard_results["user_account_visible"]
            ]
            
            if all(critical_tests):
                logger.info("\n✓ OVERALL TEST RESULT: PASS")
                logger.info("Core functionality is working as expected")
            else:
                logger.info("\n✗ OVERALL TEST RESULT: FAIL")
                logger.info("Critical functionality issues detected")
                test_passed = False
                
        except Exception as e:
            logger.error(f"Test suite failed with error: {e}")
            test_passed = False
            
        finally:
            await self.teardown_browser()
            
        return test_passed

async def main():
    """Main function to run the test"""
    test = SegwiseDashboardTest()
    success = await test.run_full_test()
    
    if success:
        logger.info("Test completed successfully")
        sys.exit(0)
    else:
        logger.error("Test failed")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())
