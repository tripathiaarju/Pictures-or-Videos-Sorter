import os
from datetime import datetime
def main():
	for folder_name in os.listdir("C:\My Stuff\Pictures"):
		path="C:\My Stuff\Pictures\{}".format(folder_name)
		i = 1
		v = 1
		for pic_name in os.listdir(path):

			timestamp = os.path.getmtime(path + "/" + pic_name)
			dt = datetime.fromtimestamp(timestamp)
			# input_date = datetime.strptime(str(dt).split()[0], '%Y-%m-%d')
			# output_date_str = input_date.strftime('%d-%b-%y')
			# print(output_date_str)
			output_date_str = str(dt).split()[0]
			if pic_name.lower().endswith(".jpg"):
				s = path+"/"+pic_name
				d = path+"/"+""+output_date_str+" - " +str(i)+".jpg"
				os.rename(s,d)
				i+=1
			if pic_name.lower().endswith(".mp4"):
				s = path+"/"+pic_name
				d = path+"/"+""+output_date_str+" - " +str(v)+".mp4"
				os.rename(s,d)
				v+=1
			if pic_name.lower().endswith(".png"):
				s = path+"/"+pic_name
				d = path+"/"+""+output_date_str+" - " +str(i)+".jpg"
				os.rename(s,d)
				i+=1
			if pic_name.lower().endswith(".webp"):
				s = path + "/" + pic_name
				d = path + "/" + "" + output_date_str +" - " + str(i) + ".jpg"
				os.rename(s, d)
				i += 1
if __name__ == '__main__':
	main()