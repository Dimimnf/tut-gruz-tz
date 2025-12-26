import { queryOptions } from "@tanstack/react-query";
import httpService from "./http.service";
import type { IContainer, IContainerFilters } from "../../interface";
// Интерфейс контейнера на основе модели бэкенда




const containersEndPoint = "/containers";

const getOneContainer = async (
    containerId: string,
    config?: { signal?: AbortSignal }
) => {
    const { data } = await httpService.get<IContainer>(
        `${containersEndPoint}/${containerId}`,
        config
    );
    return data;
};

const getAllContainers = async (
    filters?: IContainerFilters,
    config?: { signal?: AbortSignal }
) => {
    let url = containersEndPoint;
    if (filters && Object.keys(filters).length > 0) {
        // Преобразуем параметры в строку запроса
        // Используем any, чтобы URLSearchParams принял числа, или предварительно приведем к строкам
        const params = new URLSearchParams();
        Object.entries(filters).forEach(([key, value]) => {
            if (value !== undefined && value !== null) {
                params.append(key, value.toString());
            }
        });
        url += `?${params.toString()}`;
    }
    const { data } = await httpService.get<IContainer[]>(`${url}`, config);
    return data;
};

export const containersService = {
    baseKey: "containers",

    // Получение одного контейнера
    getOneContainerQueryOptions: (containerId: string) => {
        return queryOptions({
            queryKey: [containersService.baseKey, containerId],
            queryFn: (meta) => getOneContainer(containerId, meta),
        });
    },

    // Получение списка контейнеров с фильтрацией
    getContainersQueryOptions: (filters?: IContainerFilters) => {
        return queryOptions({
            queryKey: [containersService.baseKey, "list", filters],
            queryFn: (meta) => getAllContainers(filters, meta),
        });
    },
};
