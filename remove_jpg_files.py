import os

folder_path = r"C:\Users\v23ASayed2\Desktop\Vodafone\national IDs\PDV_Output_Batch_MSISDNs"

for filename in os.listdir(folder_path):
    if filename.endswith(".jpg"):
        os.remove(os.path.join(folder_path, filename))