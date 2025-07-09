#!/usr/bin/env python3
"""
Test script to verify the footer text color has been updated to #FFFFFF.
"""

import re
from pathlib import Path

def test_footer_color():
    """Test that the footer text color is set to #FFFFFF."""

    print("🧪 Testing footer text color update...")

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

    # Check that .final-cta section uses #FFFFFF
    final_cta_pattern = r'\.final-cta\s*{[^}]*color:\s*#FFFFFF[^}]*}'
    check_requirement(
        ".final-cta section uses #FFFFFF color",
        re.search(final_cta_pattern, content, re.DOTALL) is not None
    )

    # Check that .final-cta h2 uses #FFFFFF
    final_cta_h2_pattern = r'\.final-cta\s+h2\s*{[^}]*color:\s*#FFFFFF[^}]*}'
    check_requirement(
        ".final-cta h2 uses #FFFFFF color",
        re.search(final_cta_h2_pattern, content, re.DOTALL) is not None
    )

    # Check that footer uses #FFFFFF
    footer_pattern = r'footer\s*{[^}]*color:\s*#FFFFFF[^}]*}'
    check_requirement(
        "footer uses #FFFFFF color",
        re.search(footer_pattern, content, re.DOTALL) is not None
    )

    # Check that the specific text strings are present
    check_requirement(
        "First target text is present",
        "Join our community of developers and researchers pushing the boundaries of AI-powered collaborative coding!" in content
    )

    check_requirement(
        "Second target text is present",
        "Let's push the boundaries of what's possible with AI-powered collaborative coding!" in content
    )

    # Check that opacity: 0.9 has been removed from the second paragraph
    opacity_pattern = r'<p[^>]*style="[^"]*opacity:\s*0\.9[^"]*"[^>]*>Let\'s push the boundaries'
    check_requirement(
        "Opacity 0.9 removed from second target text",
        re.search(opacity_pattern, content) is None
    )

    # Print summary
    print(f"\n📊 Test Summary: {tests_passed}/{total_tests} tests passed")

    if tests_passed == total_tests:
        print("🎉 All footer color tests passed!")
        return True
    else:
        print(f"⚠️  {total_tests - tests_passed} tests failed.")
        return False

if __name__ == "__main__":
    print("🧪 Testing Footer Color Update")
    print("=" * 40)

    success = test_footer_color()

    print("\n" + "=" * 40)
    if success:
        print("🎉 SUCCESS: Footer color has been updated to #FFFFFF!")
        exit(0)
    else:
        print("❌ ISSUES FOUND: Footer color update incomplete.")
        exit(1)
