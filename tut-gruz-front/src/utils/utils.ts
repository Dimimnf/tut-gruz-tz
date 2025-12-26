import { initData, retrieveLaunchParams, retrieveRawInitData } from "@tma.js/sdk-react";

export const getUserIDAndOrUsername = () => {
  const launchParams = retrieveLaunchParams();
  const initDataRaw = import.meta.env.VITE_MODE === "DEV" ? launchParams.tgWebAppData?.user?.id.toString() as string : retrieveRawInitData() as string;
  console.log(initData.chat);

  return {
    user_id: launchParams.tgWebAppData?.user?.id.toString() as string,
    username: launchParams.tgWebAppData?.user?.username as string,
    photo_url: launchParams.tgWebAppData?.user?.photo_url as string,
    initData: initData,
    initDataRaw: initDataRaw,
  };
};