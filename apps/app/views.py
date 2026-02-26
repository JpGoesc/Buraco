import json
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from app.domain.services import CreateMatchService
from app.infrastructure.repositories import PlayerRepository, MatchRepository

@csrf_exempt # For simplicity; in production, proper CSRF handling is crucial for web apps.
@require_POST
def create_match_api(request):
    try:
        data = json.loads(request.body)
        jogador_1_id = data.get("jogador_1")
        jogador_2_id = data.get("jogador_2")

        if not all([jogador_1_id, jogador_2_id]):
            return JsonResponse({"error": "IDs dos jogadores são obrigatórios."}, status=400)

        if not isinstance(jogador_1_id, int) or not isinstance(jogador_2_id, int):
            return JsonResponse({"error": "IDs dos jogadores devem ser números inteiros."}, status=400)

        # Instantiate repositories and service
        player_repo = PlayerRepository()
        match_repo = MatchRepository()
        create_match_service = CreateMatchService(player_repo, match_repo)

        match_id = create_match_service.execute(jogador_1_id, jogador_2_id)
        return JsonResponse({"message": "Partida criada com sucesso.", "id": match_id}, status=201)

    except ValueError as e:
        return JsonResponse({"error": str(e)}, status=400)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Requisição inválida. O corpo deve ser um JSON válido."}, status=400)
    except Exception as e:
        return JsonResponse({"error": f"Ocorreu um erro interno: {str(e)}"}, status=500)
