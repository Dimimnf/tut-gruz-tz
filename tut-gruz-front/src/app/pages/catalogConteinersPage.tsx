import { useNavigate } from 'react-router-dom';

const CONTAINER_TYPES = [
  { id: '20ft', label: "20' (стандартный)" },
  { id: '40ft_hc', label: "40' HC" },
  { id: '40ft_reefer', label: "40' рефрижератор" },
];


const CatalogConteinersPage = () => {
	const navigate = useNavigate();

	const handleContainerClick = (id: string) => {
		navigate(`/catalog-containers/${id}`);
	};

	return (
		<div className="flex flex-col min-h-screen bg-gray-50 p-4 font-sans">
			<h1 className="text-2xl font-bold text-gray-800 mb-6 text-center">
				Выберите тип контейнера
			</h1>

			<div className="flex flex-col gap-4">
				{CONTAINER_TYPES.map((container) => (
					<button
						key={container.id}
						onClick={() => handleContainerClick(container.id)}
						className="w-full bg-white p-6 rounded-2xl shadow-sm border border-gray-100 hover:shadow-md active:scale-98 transition-all duration-200 flex items-center justify-between group cursor-pointer"
					>
						<span className="text-lg font-medium text-gray-700 group-hover:text-blue-600 transition-colors">
							{container.label}
						</span>
						<svg
							xmlns="http://www.w3.org/2000/svg"
							className="h-6 w-6 text-gray-400 group-hover:text-blue-500 transition-colors"
							fill="none"
							viewBox="0 0 24 24"
							stroke="currentColor"
						>
							<path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
						</svg>
					</button>
				))}
			</div>
		</div>
	);
};

export default CatalogConteinersPage;
