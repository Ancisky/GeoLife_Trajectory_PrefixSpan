if __name__ == "__main__":
    with open("test.CSV", 'r') as input:
        h=[]
        #f=open("test2.CSV",'w')
        for line in input.readlines():
            elements = line.split(',')
            if(float(elements[0])<40.0814 and float(elements[0])>40.0794 and float(elements[1])<(116.236+0.003) and float(elements[1])>(116.236-0.003)):
                #print("Have one!")
                if (len(h) == 0):
                    h.append('a')
                    continue
                if(h[-1]!='a'):
                    h.append('a')
                continue
            if (float(elements[0]) < (40.0452 + 0.001) and float(elements[0]) > (40.0452 - 0.001) and float(elements[1]) < (116.252 + 0.003) and float(elements[1]) > (116.252 - 0.003)):
                print("Have one!")
                if (len(h) == 0):
                    h.append('b')
                    continue
                if (h[-1] != 'b'):
                    h.append('b')
                continue
            if (float(elements[0]) < (40.0155 + 0.001) and float(elements[0]) > (40.0155 - 0.001) and float(elements[1]) < (116.298 + 0.003) and float(elements[1]) > (116.298 - 0.003)):
                print("Have one!")
                if(len(h)==0):
                    h.append('c')
                    continue
                if (h[-1] != 'c'):
                    h.append('c')
                continue
            if (float(elements[0]) < (39.9963 + 0.001) and float(elements[0]) > (39.9963 - 0.001) and float(elements[1]) < (116.288 + 0.003) and float(elements[1]) > (116.288 - 0.003)):
                print("Have one!")
                if (len(h) == 0):
                    h.append('d')
                    continue
                if (h[-1] != 'd'):
                    h.append('d')
                continue
            print(float(elements[0]),float(elements[1]))
        """
            elements[0] = str(int(float(elements[0]))) + "°" + str(int((float(elements[0]) - int(float(elements[0]))) * 60)) +\
            "'" + str((((float(elements[0]) - int(float(elements[0]))) * 60) - int((float(elements[0]) - int(float(elements[0]))) * 60)) * 60) +"''"+' '+'E'
            elements[1] = str(int(float(elements[1]))) + "°" + str(int((float(elements[1]) - int(float(elements[1]))) * 60)) +\
            "'" + str((((float(elements[1]) - int(float(elements[1]))) * 60) - int((float(elements[1]) - int(float(elements[1]))) * 60)) * 60) +"''"+' '+'N'+'\n'
            line1 = elements[0]+','+elements[1]
            f.write(line1)
        """
        print(h)
        #f.close()