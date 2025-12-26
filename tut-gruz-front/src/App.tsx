import { createBrowserRouter, createRoutesFromElements, Navigate, Route, RouterProvider } from 'react-router-dom';
import CatalogConteinersPage from './app/pages/catalogConteinersPage';
import OneContainerPage from './app/pages/oneContainerPage';
import ListConatainers from './app/pages/listConatainers';

const router = createBrowserRouter(
  createRoutesFromElements(
    <>
      <Route path="/" element={<Navigate to="/catalog-containers" replace />} />
      <Route path="/catalog-containers" element={<CatalogConteinersPage />} />
      <Route path="/catalog-containers/:catalog" element={<ListConatainers />} />
      <Route path="/catalog-containers/:catalog/:id" element={<OneContainerPage />} />
    </>
  )
);

function App() {
  return (
    <div className='app'>

      <RouterProvider router={router} />
      {/* <ReactQueryDevtools initialIsOpen={false} /> */}
      {/* <ToastContainer transition={Flip} autoClose={2000} closeOnClick={true} pauseOnHover={true} draggable={true} /> */}
    </div>
  )
}

export default App
