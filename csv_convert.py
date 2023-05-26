import csv
import ast
import json

frontend_data = []

#def convert_csv():
with open('sample_output.csv', 'r', newline='') as inputFile, open('output_final.csv', 'w', newline='') as writerFile:
    read_file = csv.reader(inputFile)
    write_file = csv.writer(writerFile, delimiter=',')
    for row in read_file:
        obj = {}
        lat, long, id, cost_demand, node_label = row[0], row[1], row[2], row[3], row[4]
        echelon, index = row[5], row[6]
        routes, route_costs = row[7], row[8]
        capacity, capacity_costs = row[9], row[10]
        obj['lat'], obj['lng'], obj['label'], obj['echelon'] =lat,long, node_label, echelon
        obj['routes'], obj['route_costs'] = routes, route_costs 
        
        frontend_data.append(obj)
        if routes and routes!='routes':
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
    #print(frontend_data)

with open("data_file.json", "w") as wf:
    json.dump(frontend_data[1:], wf)