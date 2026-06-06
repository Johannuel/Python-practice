#!/bin/bash

# ==============================================================================
# Script: system_manager.sh
# Descripción: Gestor de mantenimiento avanzado para Void Linux.
# ==============================================================================

# Colores para la interfaz
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Verificación de permisos de root
check_root() {
    if [[ $EUID -ne 0 ]]; then
       echo -e "${RED}[ERROR] Esta acción requiere permisos de root (sudo).${NC}"
       return 1
    fi
    return 0
}

# Función de pausa para confirmación visual
wait_user() {
    echo -e "\n${BLUE}Presiona Enter para continuar...${NC}"
    read
}

# 1. Limpieza Avanzada
perform_cleanup() {
    if ! check_root; then return; fi
    echo -e "${GREEN}>>> Iniciando limpieza profunda del sistema (Void Linux)...${NC}"

    echo -e "${YELLOW}- Limpiando caché de paquetes (xbps-remove -O)...${NC}"
    xbps-remove -O || echo -e "${RED}Error en xbps-remove -O${NC}"

    echo -e "${YELLOW}- Limpiando paquetes huérfanos (xbps-remove -o)...${NC}"
    xbps-remove -o || echo -e "${RED}Error en xbps-remove -o${NC}"

    echo -e "${YELLOW}- Liberando memoria caché del kernel...${NC}"
    sync && sysctl -w vm.drop_caches=3

    echo -e "${GREEN}>>> ¡Limpieza completada exitosamente!${NC}"
    wait_user
}

# 2. Actualización Segura
perform_update() {
    if ! check_root; then return; fi
    echo -e "${GREEN}>>> Iniciando actualización total del sistema...${NC}"

    # Sincronizar repositorios y actualizar paquetes
    xbps-install -Su || { echo -e "${RED}Error al actualizar el sistema.${NC}"; wait_user; return; }

    echo -e "${GREEN}>>> Sistema actualizado correctamente.${NC}"
    wait_user
}

# 3. Monitoreo de RAM
show_ram_usage() {
    echo -e "${BLUE}>>> Estado de la memoria RAM:${NC}"
    free -h
    wait_user
}

# 4. Monitoreo de Temperatura
show_temperature() {
    echo -e "${BLUE}>>> Lectura de temperatura del sistema:${NC}"
    if command -v sensors &> /dev/null; then
        sensors
    else
        echo -e "${YELLOW}lm-sensors no instalado.${NC}"
        echo "Instálalo con: sudo xbps-install -S lm_sensors"
    fi
    wait_user
}

# 5. Información de Disco
show_disk_usage() {
    echo -e "${BLUE}>>> Uso de espacio en disco:${NC}"
    df -h | grep '^/dev/'
    wait_user
}

# --- Menú Principal ---
show_menu() {
    clear
    echo -e "${BLUE}=========================================${NC}"
    echo -e "   Gestor de Sistema (Void Linux Pro)   "
    echo -e "${BLUE}=========================================${NC}"
    echo "1. Limpieza profunda (Caché y huérfanos)"
    echo "2. Actualizar sistema completo"
    echo "3. Medidor de RAM"
    echo "4. Medidor de Temperatura (lm-sensors)"
    echo "5. Uso de espacio en disco"
    echo "6. Salir"
    echo -e "${BLUE}=========================================${NC}"
    echo -n "Selecciona una opción [1-6]: "
}

while true; do
    show_menu
    read option
    case $option in
        1) perform_cleanup ;;
        2) perform_update ;;
        3) show_ram_usage ;;
        4) show_temperature ;;
        5) show_disk_usage ;;
        6) echo "Saliendo..."; exit 0 ;;
        *) echo -e "${RED}Opción no válida.${NC}"; sleep 1 ;;
    esac
done
