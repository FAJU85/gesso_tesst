#!/usr/bin/env python
"""Test script for MCP servers installed in this environment."""

import subprocess
import sys
import json

def test_agileforagents():
    """Test agileforagents MCP server tools."""
    print("=" * 60)
    print("Testing agileforagents MCP Server")
    print("=" * 60)
    
    try:
        from agileforagents.server import app
        from agileforagents import __version__
        print(f"[OK] Server loaded (v{__version__})")
        
        # Test get_agent_rules
        from agileforagents.environment_layer import EnvironmentLayer
        env = EnvironmentLayer()
        rules = env.get_rules_only()
        print(f"[OK] get_agent_rules: {len(rules)} characters returned")
        
        # Test feedback_stats
        from agileforagents.feedback_logger import FeedbackLogger
        logger = FeedbackLogger()
        count = logger.count()
        print(f"[OK] feedback_stats: {count} entries logged")
        
        print("\n[SUCCESS] agileforagents server is working correctly!\n")
        return True
        
    except Exception as e:
        print(f"[ERROR] {e}\n")
        return False


def test_ai_rule_learning():
    """Test ai-rule-learning-mcp server tools."""
    print("=" * 60)
    print("Testing ai-rule-learning-mcp Server")
    print("=" * 60)
    
    try:
        from ai_rule_learning_mcp.server import app
        from ai_rule_learning_mcp import __version__
        print(f"[OK] Server loaded (v{__version__})")
        
        # Test list_skills
        from ai_rule_learning_mcp.skills import list_skills
        skills = list_skills()
        print(f"[OK] list_skills: {len(skills)} skills available")
        
        # Test recall memory
        from ai_rule_learning_mcp.memory import load_memory
        memory = load_memory()
        print(f"[OK] recall: {len(memory)} memories stored")
        
        # Test load_active_rules
        from ai_rule_learning_mcp.store import load_active_rules
        rules = load_active_rules()
        print(f"[OK] get_guardrail_rules: {len(rules)} rules active")
        
        # Test detected targets
        from ai_rule_learning_mcp.injector import detected_targets
        targets = list(detected_targets())
        print(f"[OK] list_providers: {len(targets)} AI agents detected")
        for target in targets:
            print(f"  - {target.name}")
        
        print("\n[SUCCESS] ai-rule-learning-mcp server is working correctly!\n")
        return True
        
    except Exception as e:
        print(f"[ERROR] {e}\n")
        return False


def main():
    """Run all MCP server tests."""
    print("\n" + "=" * 60)
    print("MCP Server Test Suite")
    print("=" * 60 + "\n")
    
    results = {
        "agileforagents": test_agileforagents(),
        "ai-rule-learning-mcp": test_ai_rule_learning(),
    }
    
    print("=" * 60)
    print("Summary")
    print("=" * 60)
    
    for name, passed in results.items():
        status = "[PASS]" if passed else "[FAIL]"
        print(f"{status}: {name}")
    
    all_passed = all(results.values())
    print("\n" + ("All tests passed!" if all_passed else "Some tests failed."))
    
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
