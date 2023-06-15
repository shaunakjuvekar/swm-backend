import csv
import ast
import json
import math

frontend_data = []

#def convert_csv():
def main():
    print("csv_convert called from app.py")
    with open('sample_output.csv', 'r', newline='') as inputFile, open('output_final.csv', 'w', newline='') as writerFile:
        
        read_file = csv.reader(inputFile)
        write_file = csv.writer(writerFile, delimiter=',')
        row_number=0
        for row in read_file:
            obj = {}
            lat, long, id, cost_demand, node_label = row[0], row[1], row[2], row[3], row[4]
            echelon, index = row[5], row[6]
            facility_costs ,facility_sizes, vehicle_capacity =  row[7], row[8], row[9]
            routes, route_costs = row[10], row[11]
            capacity, capacity_costs = row[12], row[13]
            obj['lat'], obj['lng'], obj['label'], obj['echelon'] =lat,long, node_label, echelon
            obj['routes'], obj['route_costs'] = routes, route_costs 
           
            frontend_data.append(obj)
            if routes and row_number!=0:
                #print("routes:" , routes)
                write_file.writerow(['Facility', ' Echelon'])
                write_file.writerow([node_label, echelon])
                write_file.writerow([' ', 'Selection', 'Cost'])
                write_file.writerow(['Capacity', capacity, capacity_costs])
                write_file.writerow(['Location', node_label, cost_demand])
                write_file.writerow(['Vehicle', 'Node Label(s) served in echelon '+str(int(echelon)-1), 'Cost'])
            
               
                routes_arr = (ast.literal_eval(routes))
                costs_arr = (ast.literal_eval(route_costs))
                for i in range(len(routes_arr)):
                    write_file.writerow([i+1, routes_arr[i], costs_arr[i]])
            
                write_file.writerow([])
            row_number+=1
        #print(frontend_data)


    with open("data_file.json", "w") as wf:
        print("Writing to data_file.json")
        json.dump(frontend_data[1:], wf)
