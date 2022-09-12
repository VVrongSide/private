# Libraries to import
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# Plot object  
class Plots(object):
       """Plot class\n\n
       
       Standard plot = basic_plot
       Bar plot = 
       Hist plot = 
       Pie plot =  

       """

       def __init__(self):
              pass



############################################################################################

       def single_plot(self, args=list, tags=list):

              plt.figure()
              plt.plot(args[0],args[1], label=args[2])  
              plt.title(tags[0])
              plt.xlabel(tags[1])
              plt.ylabel(tags[2])
              plt.legend()

              plt.show()




############################################################################################

       def new_plot(self):
              
              x = np.linspace(0, 2, 100)  # Sample data.

              plt.figure()
              plt.plot(x, x, label='linear')  # Plot some data on the (implicit) axes.
              plt.plot(x, x**2, label='quadratic')  # etc.
              plt.plot(x, x**3, label='cubic')
              plt.xlabel('x label')
              plt.ylabel('y label')
              plt.title("Simple Plot")
              plt.legend()

              plt.show()




########################################
###### MAIN PROGRAM ####################
########################################

if __name__=="__main__":


       x = np.linspace(0,10,100)
       y = np.sin(2 * x)
       x2 = np.array([-5,5])
       y2 = np.sin(x)



       value = [x,x,"Graf 1"]
       name = ["Overskrift", "X label", "Y label"]

       p = Plots()

       p.single_plot(value, name)

       #p.simple_plot(x,y2,"Algorithm run-time (fantasy) ","Time (s)","Cost (c)")
       #p.new_plot()
       #p.simple_plot(x, y, title, x_label, y_label)
       