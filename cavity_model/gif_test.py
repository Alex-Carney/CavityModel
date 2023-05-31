
import cavity_gifs as cg
import static_simulation as pb
import numpy as np

# Constants
wf_sweep = np.r_[6.6:7.4:.001]
cavity_freqs = np.array([[7.0167], [7.0123]])
single_cavity_drive = np.array([[1], [0]])
J_experimentally_fitted = .02

# Things to sweep
simple_adj = np.array([[0, 1], [1, 0]])
#gamma_experimentally_fitted = np.array([[.000001], [1]])


# Sweep gamma - dissipation term

def get_abs_photon_response(gamma_val):
    gamma_experimentally_fitted = np.array([[.000001], [gamma_val]])
    cavity_model = pb.CavityModel(simple_adj, gamma_experimentally_fitted, J_experimentally_fitted, wf_sweep, cavity_freqs)
    ssr = cavity_model.cavity_steady_state(single_cavity_drive)
    complex_response = ssr(wf_sweep)
    complex_response = np.squeeze(complex_response, axis=1)
    SCALE_FACTOR = 9e-6
    return np.abs(complex_response[1, :]) * SCALE_FACTOR


# write me a range from .00001 to 1
gammas = np.linspace(.1, .001, 100)
y_data_list = [get_abs_photon_response(i) for i in gammas]
cg.create_gif(wf_sweep, y_data_list, gammas, 'wf sweep (freq)', 'transmission (arb)', 'Sweep', 'sine_waves.gif', interval=200)