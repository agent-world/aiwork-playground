#!/usr/bin/env python3
"""
Test script to verify the AI Work Playground landing page meets requirements.
"""

import re
from pathlib import Path

def test_landing_page():
    """Test the landing page HTML file for required content and structure."""

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

    # Content Requirements
    check_requirement(
        "Hero section with clear headline",
        "AI Work Playground" in content and "experimental repository" in content
    )

    check_requirement(
        "Explanation of playground's purpose",
        "testing ground" in content and "AI agents" in content
    )

    check_requirement(
        "How to participate section",
        "How to Participate" in content and "Getting started" in content
    )

    check_requirement(
        "Call to action buttons",
        "Browse Experiments" in content and "Get Started" in content
    )

    check_requirement(
        "Types of experiments section",
        "Types of Experiments" in content and "Feature Development" in content
    )

    # Technical Requirements
    check_requirement(
        "HTML5 doctype",
        content.strip().startswith("<!DOCTYPE html>")
    )

    check_requirement(
        "Responsive viewport meta tag",
        'name="viewport"' in content and 'width=device-width' in content
    )

    check_requirement(
        "Proper page title",
        "<title>" in content and "AI Work Playground" in content
    )

    check_requirement(
        "Meta description for SEO",
        'name="description"' in content
    )

    # Design Requirements
    check_requirement(
        "CSS styling included",
        "<style>" in content and "font-family" in content
    )

    check_requirement(
        "Responsive design (media queries)",
        "@media" in content and "max-width" in content
    )

    check_requirement(
        "Modern design elements (gradients, shadows)",
        "gradient" in content and "box-shadow" in content
    )

    # Accessibility Requirements
    check_requirement(
        "Semantic HTML structure",
        "<header>" in content and "<main>" in content and "<footer>" in content
    )

    check_requirement(
        "Navigation structure",
        "<nav" in content and "navigation" in content
    )

    # GitHub Integration
    check_requirement(
        "Links to GitHub issues",
        "github.com" in content and "issues" in content
    )

    check_requirement(
        "Links to GitHub discussions",
        "discussions" in content
    )

    # Interactive Features
    check_requirement(
        "JavaScript for interactivity",
        "<script>" in content and "addEventListener" in content
    )

    check_requirement(
        "Smooth scrolling implementation",
        "scroll" in content and "smooth" in content
    )

    # Content Quality
    check_requirement(
        "Emojis for visual appeal",
        "🎮" in content and "🚀" in content and "🧪" in content
    )

    check_requirement(
        "Clear section headings",
        "<h1" in content and "<h2>" in content and "<h3>" in content
    )

    check_requirement(
        "Footer with attribution",
        "AI Work ecosystem" in content and "2025" in content
    )

    # Print summary
    print(f"\n📊 Test Summary: {tests_passed}/{total_tests} tests passed")

    if tests_passed == total_tests:
        print("🎉 All tests passed! Landing page meets all requirements.")
        return True
    else:
        print(f"⚠️  {total_tests - tests_passed} tests failed. Please review the requirements.")
        return False

def test_file_structure():
    """Test that the file structure is GitHub Pages ready."""

    print("\n📁 Testing file structure...")

    # Check for index.html in root
    if Path("index.html").exists():
        print("✅ PASS: index.html exists in root directory (GitHub Pages ready)")
        return True
    else:
        print("❌ FAIL: index.html not found in root directory")
        return False

def test_performance():
    """Test basic performance characteristics."""

    print("\n⚡ Testing performance characteristics...")

    html_file = Path("index.html")
    if not html_file.exists():
        print("❌ FAIL: Cannot test performance - index.html not found")
        return False

    content = html_file.read_text()
    file_size = len(content.encode('utf-8'))

    # Check file size (should be reasonable for fast loading)
    if file_size < 100000:  # Less than 100KB
        print(f"✅ PASS: File size is reasonable ({file_size:,} bytes)")
        size_ok = True
    else:
        print(f"⚠️  WARNING: File size is large ({file_size:,} bytes)")
        size_ok = False

    # Check for external dependencies
    external_deps = 0
    if 'src="http' in content:
        external_deps += content.count('src="http')
    if 'href="http' in content and 'github.com' not in content:
        external_deps += content.count('href="http') - content.count('github.com')

    if external_deps == 0:
        print("✅ PASS: No external dependencies (fast loading)")
        deps_ok = True
    else:
        print(f"⚠️  WARNING: {external_deps} external dependencies found")
        deps_ok = False

    return size_ok and deps_ok

if __name__ == "__main__":
    print("🧪 Testing AI Work Playground Landing Page")
    print("=" * 50)

    # Run all tests
    content_test = test_landing_page()
    structure_test = test_file_structure()
    performance_test = test_performance()

    # Final summary
    print("\n" + "=" * 50)
    if content_test and structure_test and performance_test:
        print("🎉 SUCCESS: Landing page is ready for deployment!")
        exit(0)
    else:
        print("❌ ISSUES FOUND: Please address the failed tests above.")
        exit(1)
