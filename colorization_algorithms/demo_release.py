import sys
import matplotlib
import matplotlib.pyplot as plt

from .colorizers import *

# TEST - colorization_master as cwd
# filepath = "imgs/ansel_adams3.jpg"
# model_dir = "models"  # For testing from models dir
# RESULT_IMG_SAVE_PATH = "imgs_out/"

# TEST - Project dir as cwd
# filepath = "static/img/uploads/ansel_adams3.jpg"
# model_dir = "colorization_algorithms/colorization_master/models"

# Set backend to non-interactive one
# This solves MacOS + Flask + Matplotlib save img problem detailed here: https://github.com/matplotlib/matplotlib/issues/14304#issuecomment-545717061
matplotlib.use('agg') 

# Path for saving output image
RESULT_IMG_SAVE_PATH = "static/img/results_img/"


def main(filepath, model_dir):

	# load colorizers
	colorizer_eccv16 = eccv16(model_dir, pretrained=True).eval()
	colorizer_siggraph17 = siggraph17(model_dir, pretrained=True).eval()
	# if(opt.use_gpu):
	# 	colorizer_eccv16.cuda()
	# 	colorizer_siggraph17.cuda()

	# default size to process images is 256x256
	# grab L channel in both original ("orig") and resized ("rs") resolutions
	img = load_img(filepath)
	(tens_l_orig, tens_l_rs) = preprocess_img(img, HW=(256,256))
	# if(opt.use_gpu):
	# 	tens_l_rs = tens_l_rs.cuda()

	# colorizer outputs 256x256 ab map
	# resize and concatenate to original L channel
	img_bw = postprocess_tens(tens_l_orig, torch.cat((0*tens_l_orig,0*tens_l_orig),dim=1))
	out_img_eccv16 = postprocess_tens(tens_l_orig, colorizer_eccv16(tens_l_rs).cpu())
	out_img_siggraph17 = postprocess_tens(tens_l_orig, colorizer_siggraph17(tens_l_rs).cpu())

	# Save Resulting Images
	save_path = RESULT_IMG_SAVE_PATH
	plt.imsave(f'{save_path}%s_eccv16.png'%"saved", out_img_eccv16)
	plt.imsave(f'{save_path}%s_siggraph17.png'%"saved", out_img_siggraph17)

	plt.figure(figsize=(12,8))
	plt.subplot(2,2,1)
	plt.imshow(img)
	plt.title('Original')
	plt.axis('off')

	plt.subplot(2,2,2)
	plt.imshow(img_bw)
	plt.title('Input')
	plt.axis('off')

	plt.subplot(2,2,3)
	plt.imshow(out_img_eccv16)
	plt.title('Output (ECCV 16)')
	plt.axis('off')

	plt.subplot(2,2,4)
	plt.imshow(out_img_siggraph17)
	plt.title('Output (SIGGRAPH 17)')
	plt.axis('off')
	# plt.show()
	plt.savefig(save_path + "saved_result_final.png")  # Need to put full path here

if __name__ == "__main__":
	main(filepath, model_dir)