import { useQuery } from "@tanstack/react-query";
import { containersService } from "../service/container.service";
import type { IContainerFilters } from "../../interface";

export const useContainers = (filters?: IContainerFilters) => {
    const {
        data: containers,
        error,
        isLoading,

    } = useQuery({
        ...containersService.getContainersQueryOptions(filters),
    });


    return { error, isLoading, containers };
};