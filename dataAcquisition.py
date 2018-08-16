import csv
import numpy as np

def getDriveLogs(csv_path):
    """Public: get the driving log 
        
    @Param:
    csv_path: dir that contains driving logs;"""
    with open(csv_path + 'driving_log.csv', newline = '') as csvfile:
        driving_log = list(csv.reader(csvfile, skipinitialspace = True, delimiter = ',', quoting = csv.QUOTE_NONE))
    return driving_log[1:]

def isDrivingTooSlow(fSpeed):
    return fSpeed < 2.0

def getSamplePath(data_paths, aDataToUse, bUdacityData = True):
    image_paths = []
    steering_angles = []

    for i in range(len(data_paths)):
        if not aDataToUse[i]:
            print("skipping dataset: ", i)
            continue
        driving_log = getDriveLogs(data_paths[i])

        for line in driving_log:
            if isDrivingTooSlow(float(line[6])):
                continue
            
            fCorrection = 0.20
            fSteeringAngle = float(line[3])
            if bUdacityData:
                image_paths.append(data_paths[i] + line[0]) # center image
                steering_angles.append(fSteeringAngle)

                image_paths.append(data_paths[i] + line[1]) # right
                steering_angles.append(fSteeringAngle + fCorrection)
                
                image_paths.append(data_paths[i] + line[2]) # left
                steering_angles.append(fSteeringAngle - fCorrection)
            else:
                image_paths.append(line[0])
                steering_angles.append(fSteeringAngle)
                
                image_paths.append(line[1])
                steering_angles.append(fSteeringAngle + fCorrection)
                
                image_paths.append(line[2])
                steering_angles.append(fSteeringAngle - fCorrection)
    image_paths = np.array(image_paths)
    steering_angles = np.array(steering_angles)

    return image_paths, steering_angles