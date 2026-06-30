#!/usr/bin/env python
"""
Sync GitHub Repository to HuggingFace Space

This script helps you:
1. Check HuggingFace authentication
2. Create a Space (if needed)
3. Upload files from your project to the Space
4. Set up automatic GitHub sync

Usage:
    python sync-to-huggingface.py
"""

import subprocess
import sys
import os
from pathlib import Path

def check_hf_auth():
    """Check if user is authenticated with HuggingFace."""
    print("=" * 60)
    print("Checking HuggingFace Authentication")
    print("=" * 60)
    
    try:
        result = subprocess.run(
            ["hf", "auth", "whoami"],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        if result.returncode == 0:
            print(f"✓ Logged in as: {result.stdout.strip()}")
            return True
        else:
            print("✗ Not logged in to HuggingFace")
            return False
            
    except FileNotFoundError:
        print("✗ HuggingFace CLI not found. Install with: pip install huggingface_hub")
        return False
    except Exception as e:
        print(f"✗ Error: {e}")
        return False


def login_hf():
    """Authenticate with HuggingFace."""
    print("\n" + "=" * 60)
    print("HuggingFace Login")
    print("=" * 60)
    print("\n1. Go to: https://huggingface.co/settings/tokens")
    print("2. Create a new token with 'Write' permission")
    print("3. Copy the token (starts with hf_...)")
    print()
    
    try:
        subprocess.run(["hf", "auth", "login"], timeout=300)
        print("\n✓ Login successful!")
        return True
    except Exception as e:
        print(f"\n✗ Login failed: {e}")
        return False


def create_space(owner, space_name, sdk="static", private=False):
    """Create a new HuggingFace Space."""
    print(f"\n" + "=" * 60)
    print(f"Creating Space: {owner}/{space_name}")
    print("=" * 60)
    
    try:
        cmd = [
            "huggingface-cli", "repo", "create",
            f"{owner}/{space_name}",
            "--type", "space",
            "--sdk", sdk
        ]
        
        if private:
            cmd.append("--private")
        
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            print(f"✓ Space created: https://huggingface.co/spaces/{owner}/{space_name}")
            return True
        else:
            print(f"Note: {result.stderr.strip()}")
            print("Space may already exist or needs manual creation.")
            return False
            
    except Exception as e:
        print(f"✗ Error creating space: {e}")
        print("\nPlease create space manually at: https://huggingface.co/new-space")
        return False


def upload_files(space_id, source_dir=".", files=None):
    """Upload files to HuggingFace Space."""
    print(f"\n" + "=" * 60)
    print(f"Uploading files to {space_id}")
    print("=" * 60)
    
    if files is None:
        # Default files to upload
        files = [
            "volcanic-sand-funnel.html",
            "volcanic-sand-landing.html",
            "README.md",
            ".gitignore"
        ]
    
    try:
        from huggingface_hub import HfApi
        
        api = HfApi()
        source_path = Path(source_dir)
        
        uploaded = []
        for file in files:
            file_path = source_path / file
            if file_path.exists():
                print(f"  Uploading: {file}")
                api.upload_file(
                    path_or_fileobj=str(file_path),
                    path_in_repo=file,
                    repo_id=space_id,
                    repo_type="space"
                )
                uploaded.append(file)
            else:
                print(f"  Skipped (not found): {file}")
        
        print(f"\n✓ Uploaded {len(uploaded)} files to https://huggingface.co/spaces/{space_id}")
        return True
        
    except ImportError:
        print("✗ huggingface_hub not installed. Run: pip install huggingface_hub")
        return False
    except Exception as e:
        print(f"✗ Upload failed: {e}")
        return False


def setup_github_sync(space_name, github_owner="FAJU85", github_repo="gesso_tesst"):
    """Provide instructions for setting up GitHub sync."""
    print("\n" + "=" * 60)
    print("GitHub Sync Setup Instructions")
    print("=" * 60)
    print(f"""
To enable automatic sync between GitHub and your Space:

1. Go to your Space: https://huggingface.co/spaces/FAJU85/{space_name}

2. Click "Settings" → "Connected Repositories"

3. Click "Connect GitHub Repository"

4. Select: {github_owner}/{github_repo}

5. Branch: main

6. Click "Connect"

After setup, every push to GitHub will auto-deploy to your Space!

Space URL: https://huggingface.co/spaces/FAJU85/{space_name}
    """)


def main():
    """Main sync workflow."""
    print("\n" + "=" * 60)
    print("  HuggingFace Space Sync Tool")
    print("  GitHub: FAJU85/gesso_tesst")
    print("=" * 60)
    
    # Configuration
    HF_OWNER = "FAJU85"
    SPACE_NAME = "gesso-tesst"
    GITHUB_REPO = "gesso_tesst"
    SDK = "static"  # For HTML landing pages
    
    # Step 1: Check authentication
    if not check_hf_auth():
        choice = input("\nDo you want to login to HuggingFace? (y/n): ").strip().lower()
        if choice == 'y':
            if not login_hf():
                print("\n✗ Authentication required. Exiting.")
                return 1
        else:
            print("\n Continuing without authentication (limited functionality)")
    
    # Step 2: Create Space (optional)
    print("\n" + "=" * 60)
    print("Space Creation")
    print("=" * 60)
    print(f"\nSpace: {HF_OWNER}/{SPACE_NAME}")
    print(f"SDK: {SDK} (for static HTML pages)")
    
    choice = input("\nDo you want to create this Space now? (y/n): ").strip().lower()
    if choice == 'y':
        create_space(HF_OWNER, SPACE_NAME, SDK)
    else:
        print("\nSkipping Space creation. You can create it manually at:")
        print("https://huggingface.co/new-space")
    
    # Step 3: Upload files
    print("\n" + "=" * 60)
    print("File Upload")
    print("=" * 60)
    
    choice = input(f"\nUpload files to {HF_OWNER}/{SPACE_NAME}? (y/n): ").strip().lower()
    if choice == 'y':
        space_id = f"{HF_OWNER}/{SPACE_NAME}"
        upload_files(space_id)
    
    # Step 4: GitHub sync setup
    setup_github_sync(SPACE_NAME, HF_OWNER, GITHUB_REPO)
    
    # Summary
    print("\n" + "=" * 60)
    print("  Summary")
    print("=" * 60)
    print(f"""
✓ Files ready in: C:\\all_proj
✓ GitHub Repo: https://github.com/{HF_OWNER}/{GITHUB_REPO}
✓ Space URL: https://huggingface.co/spaces/{HF_OWNER}/{SPACE_NAME}

Next Steps:
1. Create Space at https://huggingface.co/new-space (if not done)
2. Connect GitHub repo in Space Settings
3. Push updates to GitHub to auto-deploy
    """)
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
