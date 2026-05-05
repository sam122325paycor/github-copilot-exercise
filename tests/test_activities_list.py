def test_get_activities_returns_dictionary(client):
    # Arrange
    path = "/activities"

    # Act
    response = client.get(path)

    # Assert
    assert response.status_code == 200
    payload = response.json()
    assert isinstance(payload, dict)
    assert "Chess Club" in payload


def test_each_activity_has_required_fields(client):
    # Arrange
    required_fields = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    payload = response.json()
    for name, activity in payload.items():
        assert required_fields.issubset(activity.keys()), f"Missing fields for activity: {name}"
        assert isinstance(activity["participants"], list), f"participants should be a list: {name}"
