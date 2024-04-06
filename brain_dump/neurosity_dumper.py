# from datetime import datetime
# from neurosity import NeurositySDK
# from dotenv import load_dotenv
# from pathlib import Path
# import os

# load_dotenv()
# DUMPS_DIR = Path("./dumps")


# def dump_datapoints(lines: list[dict], dump_file: TextIO) -> None:
#     for line in lines:
#         dump_file.write(json.dumps(line))
#         dump_file.write("\n")


# def init_neurosity() -> NeurositySDK:
#     neurosity = NeurositySDK(
#         {
#             "device_id": os.getenv("NEUROSITY_DEVICE_ID"),
#         }
#     )
#     neurosity.login(
#         {
#             "email": os.getenv("NEUROSITY_EMAIL"),
#             "password": os.getenv("NEUROSITY_PASSWORD"),
#         }
#     )
#     return neurosity


# def main() -> None:
#     neurosity = init_neurosity()
#     filename = str(datetime.now())
#     dump_path = DUMPS_DIR / f"{filename}.jsonl"
#     dump_meta_path = DUMPS_DIR / f"{filename}_meta.json"

#     unsubscribe = neurosity.brainwaves_raw(callback)

#     try:
#         with open(dump_path, "w") as dump_file, open(
#             dump_meta_path, "w"
#         ) as dump_meta_file:
#             pass

#         def callback(data):
#             dump_datapoints(data, dump_file)

#     except Exception as e:
#         print("fatal error:", e)
#     finally:
#         print("Unsubscribing")
#         unsubscribe()
