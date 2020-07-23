import resumegen.resume_info as resume_info
from resumegen import *
import os
import os

import resumegen.resume_info as resume_info
from resumegen import *

RESUME_SAVE_DIR = os.path.expanduser("~/Desktop")

RESUME_GEN_MAP = [(OriginalResumeGenerator, "Shawn_Shroyer_Resume.docx")]

for SAVE_MAPPING in RESUME_GEN_MAP:
    save_location = os.path.join(RESUME_SAVE_DIR, SAVE_MAPPING[1])
    with SAVE_MAPPING[0](resume_info, save_location) as file_control:
        print("Saved", save_location)
