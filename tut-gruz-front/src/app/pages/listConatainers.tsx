import { useParams, useNavigate } from 'react-router-dom';
import { useContainers } from '../hooks/useContainers';

const ListConatainers = () => {
    const { catalog } = useParams<{ catalog: string }>();
    const navigate = useNavigate();

    const { containers, isLoading, error } = useContainers({
        type: catalog
    });

    if (isLoading) {
        return (
            <div className="flex flex-col items-center justify-center min-h-screen bg-gray-50">
                <div className="w-12 h-12 border-4 border-blue-200 border-t-blue-600 rounded-full animate-spin mb-4"></div>
                <p className="text-gray-500 font-medium">Загрузка контейнеров...</p>
            </div>
        );
    }

    if (error) {
        return (
            <div className="flex flex-col items-center justify-center min-h-screen bg-gray-50 p-4">
                <div className="text-red-500 text-xl font-bold mb-2">Ошибка</div>
                <p className="text-gray-600 text-center mb-4">Не удалось загрузить список контейнеров.</p>
                <button
                    onClick={() => window.location.reload()}
                    className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition"
                >
                    Попробовать снова
                </button>
            </div>
        );
    }

    return (
        <div className="min-h-screen bg-gray-50 p-4">
            <header className="flex items-center mb-6">
                <button
                    onClick={() => navigate(-1)}
                    className="mr-4 p-2 rounded-full hover:bg-gray-200 transition"
                >
                    <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6 text-gray-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 19l-7-7 7-7" />
                    </svg>
                </button>
                <h1 className="text-xl font-bold text-gray-800">
                    {catalog === '20_std' ? "20' Стандартные" :
                        catalog === '40_hc' ? "40' High Cube" :
                            catalog === '40_ref' ? "40' Рефрижераторы" :
                                "Контейнеры"}
                </h1>
            </header>

            {!containers || containers.length === 0 ? (
                <div className="text-center py-10 text-gray-500">
                    В данной категории пока нет контейнеров.
                </div>
            ) : (
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                    {containers.map((container) => (
                        <div
                            key={container.id}
                            onClick={() => navigate(`/catalog-containers/${catalog}/${container.id}`)}
                            className="bg-white rounded-xl shadow-sm overflow-hidden active:scale-[0.99] transition-transform cursor-pointer border border-gray-100"
                        >
                            <div className="aspect-video bg-gray-200 relative overflow-hidden">
                                {container.images && container.images.length > 0 ? (
                                    <img
                                        src={container.images[0]}
                                        alt={container.short_description}
                                        className="w-full h-full object-cover"
                                    />
                                ) : (
                                    <div className="flex items-center justify-center h-full text-gray-400">
                                        <svg xmlns="http://www.w3.org/2000/svg" className="h-12 w-12" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1} d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z" />
                                        </svg>
                                    </div>
                                )}
                                <div className="absolute top-2 right-2 bg-black/60 text-white px-2 py-1 rounded text-xs font-medium">
                                    {container.type}
                                </div>
                            </div>

                            <div className="p-4">
                                <h3 className="font-semibold text-gray-800 mb-2 line-clamp-1">{container.short_description}</h3>

                                <div className="flex items-center justify-between mt-3">
                                    <span className="text-xl font-bold text-blue-700">
                                        {container.price.toLocaleString()} {container.currency}
                                    </span>
                                </div>
                            </div>
                        </div>
                    ))}
                </div>
            )}
        </div>
    );
};

export default ListConatainers;