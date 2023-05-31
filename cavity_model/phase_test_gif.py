
import cavity_gifs as cg
import static_simulation as pb
import numpy as np
import matplotlib.pyplot as plt

# Constants
wf_sweep = np.r_[6.6:7.4:.001]
cavity_freqs = np.array([[7.0167], [7.0123]])
single_cavity_drive = np.array([[1], [0]])
J_experimentally_fitted = .01
gamma_experimentally_fitted = np.array([[.01], [.01]])

# Things to sweep

#gamma_experimentally_fitted = np.array([[.000001], [1]])


# Sweep gamma - dissipation term
phase_offset = 2.56
def get_abs_photon_response(phase_val):
    simple_adj = np.array([[0, np.exp(1j * (phase_offset + phase_val))], [1, 0]])
    cavity_model = pb.CavityModel(simple_adj, gamma_experimentally_fitted, J_experimentally_fitted, wf_sweep, cavity_freqs)
    ssr = cavity_model.cavity_steady_state(single_cavity_drive)
    complex_response = ssr(wf_sweep)
    complex_response = np.squeeze(complex_response, axis=1)
    SCALE_FACTOR = .001
    return np.abs(complex_response[1, :]) * SCALE_FACTOR

#write me outer for loop for J = 0.01 to 0.1 step of .1
Js = np.linspace(0.01, 0.1, 10)
for J in Js:
    J_experimentally_fitted = J
    phases = np.linspace(0, 2*np.pi, 100)
    y_data_list = [get_abs_photon_response(i) for i in phases]

    X, Y = np.meshgrid(phases, wf_sweep)
    plt.pcolormesh(X, Y, np.transpose(np.log(y_data_list)), shading='auto')
    plt.xlabel("Phi + Phi Offset")
    plt.ylabel("Transmission Freq (GHz)")
    # make the title include (J/gamma) ratio = ()
    # title the plot to include (J/gamma) ratio = value
    plt.title("J/gamma = " + str(J_experimentally_fitted/gamma_experimentally_fitted[0, 0]))
    plt.show()

#cg.create_gif(wf_sweep, y_data_list, phases, 'wf sweep (freq)', 'transmission (arb)', 'Sweep', 'phase_sweep.gif', interval=200)