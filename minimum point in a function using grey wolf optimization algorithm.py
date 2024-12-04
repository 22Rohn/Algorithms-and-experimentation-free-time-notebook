import numpy as np
def comp_function(x):
    return np.sum(x**3 + 2*x**2 - 6*x)  # finding minimum point for the function f(x)= x^3 +2x^2-6x

def gwo(num_wolves,num_iters,dim):
    np.random.seed(42)   # to eliminate randomness at each output run

    positions =np.random.uniform(-15,10,(num_wolves,dim))
    alpha_pos=np.inf* np.ones(dim) #1st best position
    beta_pos=np.inf* np.ones(dim)  #2nd best position
    delta_pos=np.inf* np.ones(dim) #3rd best position
    alpha=np.inf   #introducing these points at point closer to infinity so we can converge to smallest point through n iterations or (fitness position)
    beta=np.inf
    delta=np.inf

    a=2
    best_position= None
    best_fitness = np.inf

    for t in range(num_iters):
        a= 2 - t*(2/num_iters)

        for i in range(num_wolves):
            fitness =  comp_function(positions[i,:])

            if fitness < alpha:
                alpha = fitness
                alpha_pos= positions[i,:].copy()
            elif fitness< beta:
                beta = fitness
                beta_pos=positions[i,:].copy()
            elif fitness <delta:
                delta = fitness
                delta_pos =positions[i,:].copy()

        for i in range(num_wolves):
            r1=np.random.rand(dim)  # randomness introduced to ensure wolves don't get struck in local minima and move forwards
            r2=np.random.rand(dim)
            A1 = 2*a*r1-a
            C1= 2*r2
            D_alpha =np.abs(C1*alpha_pos - positions[i,:])
            X1 = alpha_pos - A1*D_alpha   # updating the position of each wolves  from alpha wolf

            r1= np.random.rand(dim)
            r2= np.random.rand(dim)
            A2= 2*a*r1 -a
            C2 = 2*r2
            D_beta =np.abs(C2*beta_pos - positions[i,:])
            X2 = beta_pos - A2*D_beta # updating the position of wolves from beta wolf

            r1 = np.random.rand(dim)
            r2=np.random.rand(dim)
            A3= 2*a*r1 -a
            C3= 2*r2
            D_delta =np.abs(C3*delta_pos - positions[i,:])
            X3 = delta_pos -A3*D_delta

            positions[i,:]= (X1 + X2 + X3)/3   # updated position of wolf (actual)

        if alpha < best_fitness:
            best_fitness = alpha
            best_position = alpha_pos.copy()

        print(f"Iteration {t+1}/{num_iters} : Best Fitness = {best_fitness} , Best Position = {best_position}")
    return best_fitness ,best_position 

num_wolves =25
num_iters = 250
dim = 2

best_fitness, best_position = gwo(num_wolves, num_iters, dim)
print(f"\nFinal Best Fitness: {best_fitness}")
print(f"Final Best Position: {best_position}")       

#
            

