import axios from "axios";
import { getUserIDAndOrUsername } from "../../utils/utils";

const API_URL = import.meta.env.VITE_API;
const { initDataRaw } = getUserIDAndOrUsername()
export const mainAxios = axios.create({
  baseURL: API_URL,
  headers: {
    "Content-Type": "application/json",
    "Accept-Language": "ru",
    "X-Environment": import.meta.env.VITE_MODE,
    "X-Init-Data": initDataRaw
  },
});




const httpService = {
  get: mainAxios.get,
  post: mainAxios.post,
  put: mainAxios.put,
  delete: mainAxios.delete,
  patch: mainAxios.patch,
};

export default httpService;
