#!/usr/bin/env python3
"""
Script to get the effective URL from a redirect chain, similar to curl -w "%{url_effective}"
"""

import requests
import logging
import os
from datetime import datetime
from typing import Optional


def get_effective_url(url: str, timeout: int = 30) -> Optional[str]:
    """
    Get the effective URL after following redirects.
    
    Args:
        url: The initial URL to check
        timeout: Request timeout in seconds
        
    Returns:
        The effective URL after redirects, or None if request fails
    """
    try:
        response = requests.get(url, allow_redirects=True, timeout=timeout)
        return response.url
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None


def setup_logging():
    """Set up logging configuration"""
    log_level = os.getenv('LOG_LEVEL', 'INFO')
    logging.basicConfig(
        level=getattr(logging, log_level.upper()),
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler('app.log') if os.path.exists('.') else logging.NullHandler()
        ]
    )


def main():
    """Main function to get effective URL from picsum.photos"""
    setup_logging()
    
    url = "https://picsum.photos/800/1000"
    logging.info(f"Getting effective URL for: {url}")
    
    effective_url = get_effective_url(url)
    
    if effective_url:
        logging.info(f"Effective URL: {effective_url}")
        print(f"[{datetime.now().isoformat()}] {effective_url}")
    else:
        logging.error("Failed to get effective URL")
        print(f"[{datetime.now().isoformat()}] Failed to get effective URL")
        exit(1)


if __name__ == '__main__':
    main()
