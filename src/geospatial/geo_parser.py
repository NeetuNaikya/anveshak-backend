def parse_geospatial_query(query):
    """
    Parses a geospatial query to extract location and time information.
    
    Args:
        query (str): The user query containing geospatial information.
    
    Returns:
        dict: A dictionary containing extracted location and time information.
    """
    # Placeholder for parsed results
    parsed_results = {
        "location": None,
        "time": None
    }
    
    # Example parsing logic (to be expanded)
    if "in" in query:
        location_start = query.index("in") + 3
        location_end = query.find(" ", location_start)
        if location_end == -1:
            location_end = len(query)
        parsed_results["location"] = query[location_start:location_end]
    
    if "June" in query or "2022" in query:
        parsed_results["time"] = "June 2022"
    
    return parsed_results

def connect_to_spatial_metadata(location, time):
    """
    Connects the parsed location and time to spatial metadata.
    
    Args:
        location (str): The location extracted from the query.
        time (str): The time extracted from the query.
    
    Returns:
        str: A message indicating the connection to spatial metadata.
    """
    # Placeholder for actual spatial metadata connection logic
    return f"Connected to spatial metadata for {location} during {time}."