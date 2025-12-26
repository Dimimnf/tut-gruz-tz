import { createRoot } from 'react-dom/client'
import './assets/index.css'
import App from './App.tsx'
import { QueryClientProvider } from '@tanstack/react-query'
import { queryClient } from './myQueryClient'
import { backButton, init, themeParams, viewport, mockTelegramEnv } from '@tma.js/sdk-react';

const mockV3 = () => {
  const initDataRaw = new URLSearchParams([
    ['user', JSON.stringify({
      id: 738574104,
      first_name: 'Dmitrii',
      last_name: 'Dmitrii',
      username: '@daniyl_montego',
      language_code: 'en',
      photo_url: 'https://t.me/i/userpic/320/AHHeSt5uV4JVeGwEyzwTsm-s9qewgfbzNq0EyrmklAw.svg',

      is_premium: true,
      allows_write_to_pm: true,
    })],
    ['hash', '89d6079ad6762351f38c6dbbc41bb53048019256a9443988af7a48bcad16ba31'],
    ['auth_date', '1716922846'],
    ['start_param', 'debug'],
    ['signature', 'abc'],
    ['chat_type', 'sender'],
    ['chat_instance', '8428209589180549439'],
  ]).toString();

  mockTelegramEnv({
    launchParams: {
      tgWebAppThemeParams: {
        accentTextColor: '#6ab2f2',
        bgColor: '#17212b',
        buttonColor: '#5288c1',
        buttonTextColor: '#ffffff',
        destructiveTextColor: '#ec3942',
        headerBgColor: '#17212b',
        hintColor: '#708499',
        linkColor: '#6ab3f3',
        secondaryBgColor: '#232e3c',
        sectionBgColor: '#17212b',
        sectionHeaderTextColor: '#6ab3f3',
        subtitleTextColor: '#708499',
        textColor: '#f5f5f5'
      },
      tgWebAppPlatform: 'tdesktop',
      tgWebAppVersion: '7.2',
      tgWebAppData: initDataRaw,
    }
  });

}


const startEnvOrReal = () => {

  if (import.meta.env.VITE_MODE === 'DEV') {

    mockV3()

  }
  else {
    init()
    backButton.mount();
    backButton.show();
    backButton.onClick(() => {
      // toast.success('Назад')
      window.history.back(); // Перемещение назад в истории
    })
    viewport.mount()
    themeParams.mount()
    viewport.expand()
  }

}
startEnvOrReal()

createRoot(document.getElementById('root')!).render(

    <QueryClientProvider client={queryClient}>
      <App />
    </QueryClientProvider>

)
