from probApp import ProbApp

N = 10000

if __name__ == "__main__":
    print("Starting ...")
    pb= ProbApp()
    
    pb.monte_carlo(N, display=True)
    pb.glouton_random(N)
    pb.recuit(N, beta=5, eps=0.1)

    print("Done !")