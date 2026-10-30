import math

def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0
    
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    
    a = math.sin(dphi / 2.0)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2.0)**2
    c = 2.0 * math.atan2(math.sqrt(a), math.sqrt(1.0 - a))
    
    return R * c

def geo_filter(data, target_lat, target_lng, max_distance, filter = None):
    results = []
    
    for point in data:
        lat_str = point.get("lat")
        lng_str = point.get("lng")
        
        if lat_str is None or lng_str is None:
            continue
            
        try:
            p_lat = float(lat_str)
            p_lng = float(lng_str)
        except ValueError:
            continue
            
        calculated_dist = haversine(target_lat, target_lng, p_lat, p_lng)
        
        point["dist"] = str(calculated_dist)
        
        mats = True
        if filter:
            for material in filter:
                if material not in point.get("materials", []):
                    mats = False
        
        if calculated_dist < max_distance and mats:
            results.append((calculated_dist, point))
            
    results.sort(key=lambda x: x[0])

    return [point for dist, point in results]