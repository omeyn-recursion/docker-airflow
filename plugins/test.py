# import asyncio
# from aiopath import AsyncPath
# import time
# import os
# from typing import Tuple, Dict, Any, Optional, List

# async def main():
#     path = AsyncPath("/tmp/foo.bar")
#     while True:
#         await asyncio.sleep(5)
#         print(os.listdir("/tmp/"))
#         if await path.exists():
#             print("GOT FILE")
#             break
#         else:
#             print("no file")
    
# asyncio.run(main())