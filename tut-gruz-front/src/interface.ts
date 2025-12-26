// Параметры фильтрации
export interface IContainerFilters {
    type?: string;
    price_min?: number;
    price_max?: number;
}

export interface IContainer {
    id: string;
    type: string;
    slug: string;
    price: number;
    currency: string;
    short_description: string;
    description: string;
    images: string[];
}