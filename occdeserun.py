def find_element_by_css_selector(driver, name, ignore_message=False):
    """Finds an element by its CSS selector.

    Args:
        driver: The WebDriver instance to use.
        name: The CSS selector to use.
        ignore_message: Whether to ignore an error message if the element is not
            found.

    Returns:
        The WebElement object if the element is found, or None otherwise.
    """

    try:
        return driver.find_element_by_css_selector(name)
    except NoSuchElementException:
        if not ignore_message:
            logging.error('Element not found: %s', name)
        return None

