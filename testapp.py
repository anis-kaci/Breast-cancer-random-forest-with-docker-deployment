import requests

'''
    Features : 
        mean_radius
        mean_texture
        mean_perimeter
        mean_area
        mean_smoothness
        mean_compactness
        mean_concavity
        mean_concave_points
        mean_symmetry
        mean_fractal_dimension
        radius_error
        texture_error
        perimeter_error
        area_error
        smoothness_error
        compactness_error
        concavity_error
        concave_points_error
        symmetry_error
        fractal_dimension_error
        worst_radius
        worst_texture
        worst_perimeter
        worst_area
        worst_smoothness
        worst_compactness
        worst_concavity
        worst_concave_points
        worst_symmetry
        worst_fractal_dimension
'''
data = {
    
    "features": [20.78, 18.45, 100.00, 800.00, 0.102, 0.120, 0.088, 0.040, 0.178, 0.058, 0.460, 1.104, 3.647, 60.36, 0.0067, 0.040, 0.037, 0.015, 0.026, 0.004, 16.27, 27.92, 135.10, 1236.00, 0.124, 0.249, 0.219, 0.093, 0.253, 0.065]
}


response = requests.post("http://localhost:5000/predict", json=data)

result = response.json()

percentage = result['probability'] * 100

if(result['prediction'] == 0):
    print("The tumor you described is not malignant with  " + str(percentage) + "% confidence")
else:
    print("The tumor you described is malignant with  " + str(percentage) + "% confidence")

