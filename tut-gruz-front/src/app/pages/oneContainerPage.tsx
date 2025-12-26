import { useParams, useNavigate } from 'react-router-dom';
import { useOneContainer } from '../hooks/useOneContainer';
import { useState } from 'react';

const OneContainerPage = () => {
    const { id } = useParams<{ id: string }>();
    const navigate = useNavigate();
    const [activeImageIndex, setActiveImageIndex] = useState(0);

    const { container, isLoading, error } = useOneContainer(id || '');

    if (isLoading) {
        return (
            <div className="flex flex-col items-center justify-center min-h-screen bg-gray-50">
                <div className="w-12 h-12 border-4 border-blue-200 border-t-blue-600 rounded-full animate-spin mb-4"></div>
                <p className="text-gray-500 font-medium">Загрузка информации о контейнере...</p>
            </div>
        );
    }

    if (error || !container) {
        return (
            <div className="flex flex-col items-center justify-center min-h-screen bg-gray-50 p-4">
                <div className="text-red-500 text-xl font-bold mb-2">Ошибка</div>
                <p className="text-gray-600 text-center mb-4">Не удалось загрузить данные контейнера.</p>
                <button
                    onClick={() => navigate(-1)}
                    className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition"
                >
                    Вернуться назад
                </button>
            </div>
        );
    }

    return (
        <div className="min-h-screen bg-gray-50 p-4 pb-20">
            <header className="flex items-center mb-6">
                <button
                    onClick={() => navigate(-1)}
                    className="mr-4 p-2 rounded-full hover:bg-gray-200 transition"
                >
                    <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6 text-gray-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 19l-7-7 7-7" />
                    </svg>
                </button>
                <h1 className="text-lg font-bold text-gray-800 line-clamp-1">
                    {container.short_description}
                </h1>
            </header>

            <div className="bg-white rounded-2xl shadow-sm overflow-hidden mb-6">
                {/* Main Image */}
                <div className="aspect-video bg-gray-200 relative">
                    {container.images && container.images.length > 0 ? (
                        <img
                            src={container.images[activeImageIndex]}
                            alt={container.short_description}
                            className="w-full h-full object-cover"
                        />
                    ) : (
                        <div className="flex items-center justify-center h-full text-gray-400">
                            <svg xmlns="http://www.w3.org/2000/svg" className="h-16 w-16" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1} d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z" />
                            </svg>
                        </div>
                    )}
                </div>

                {/* Thumbnails */}
                {container.images && container.images.length > 1 && (
                    <div className="flex gap-2 p-4 overflow-x-auto">
                        {container.images.map((img, idx) => (
                            <button
                                key={idx}
                                onClick={() => setActiveImageIndex(idx)}
                                className={`flex-shrink-0 w-20 h-14 rounded-lg overflow-hidden border-2 transition ${activeImageIndex === idx ? 'border-blue-600' : 'border-transparent'
                                    }`}
                            >
                                <img src={img} alt="" className="w-full h-full object-cover" />
                            </button>
                        ))}
                    </div>
                )}
            </div>

            <div className="bg-white rounded-2xl shadow-sm p-6 mb-6">
                <div className="flex items-baseline justify-between mb-4">
                    <span className="text-2xl font-bold text-blue-700">
                        {container.price.toLocaleString()} {container.currency}
                    </span>
                    <span className="text-sm text-gray-500 bg-gray-100 px-2 py-1 rounded">
                        {container.type}
                    </span>
                </div>

                <div className="prose prose-sm max-w-none text-gray-600">
                    <h3 className="text-lg font-semibold text-gray-800 mb-2">Описание</h3>
                    <p className="whitespace-pre-line">{container.description}</p>
                </div>
            </div>

            {/* <div className="fixed bottom-0 left-0 right-0 p-4 bg-white border-t border-gray-100 flex gap-3">
                <button className="flex-1 bg-blue-600 text-white py-3 rounded-xl font-semibold active:scale-98 transition shadow-lg shadow-blue-200">
                    Оставить заявку
                </button>
            </div> */}
        </div>
    );
};

export default OneContainerPage;