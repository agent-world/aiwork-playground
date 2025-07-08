#!/usr/bin/env python3
"""
Test script to verify the logo update implementation.
"""

import re
from pathlib import Path

def test_logo_implementation():
    """Test that the logo has been properly updated with the new image."""

    # Read the HTML file
    html_file = Path("index.html")
    if not html_file.exists():
        print("❌ FAIL: index.html file not found")
        return False

    content = html_file.read_text()

    # Test results
    tests_passed = 0
    total_tests = 0

    def check_requirement(description, condition):
        nonlocal tests_passed, total_tests
        total_tests += 1
        if condition:
            print(f"✅ PASS: {description}")
            tests_passed += 1
        else:
            print(f"❌ FAIL: {description}")

    # Logo Implementation Tests
    check_requirement(
        "Logo image element exists",
        '<img src="new_logo.jpg"' in content
    )

    check_requirement(
        "Logo has proper alt text",
        'alt="AI Work Logo"' in content
    )

    check_requirement(
        "Logo container has proper structure",
        '<div class="logo">' in content and '<span class="logo-text">' in content
    )

    check_requirement(
        "Logo CSS styling exists",
        '.logo img {' in content and 'height: 40px;' in content
    )

    check_requirement(
        "Responsive logo styles exist",
        '.logo img {' in content and 'height: 32px;' in content
    )

    check_requirement(
        "Logo text styling exists",
        '.logo-text {' in content and 'font-size: 1.5rem;' in content
    )

    check_requirement(
        "Logo file exists",
        Path("new_logo.jpg").exists()
    )

    # Verify the logo file is a valid image
    logo_file = Path("new_logo.jpg")
    if logo_file.exists():
        file_size = logo_file.stat().st_size
        check_requirement(
            "Logo file has reasonable size",
            1000 < file_size < 50000  # Between 1KB and 50KB
        )
    else:
        total_tests += 1
        print("❌ FAIL: Logo file has reasonable size")

    # Print summary
    print(f"\n📊 Logo Test Summary: {tests_passed}/{total_tests} tests passed")

    if tests_passed == total_tests:
        print("🎉 All logo tests passed! Logo implementation is successful.")
        return True
    else:
        print(f"⚠️  {total_tests - tests_passed} logo tests failed.")
        return False

if __name__ == "__main__":
    print("🧪 Testing Logo Update Implementation")
    print("=" * 50)

    success = test_logo_implementation()

    print("\n" + "=" * 50)
    if success:
        print("🎉 SUCCESS: Logo has been successfully updated!")
        exit(0)
    else:
        print("❌ ISSUES FOUND: Please review the failed tests above.")
        exit(1)
